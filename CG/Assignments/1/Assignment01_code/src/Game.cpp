#include <imgui_impl_glfw_gl3.h>
#include "Game.hpp"
#include "utitliy.hpp"
#include <algorithm>
#include <GLFW/glfw3.h>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <cmath>

bool checkCollision(GLfloat ballX, GLfloat ballY, GLfloat ballR, GLfloat playerX, GLfloat playerY, GLfloat playerSizeX, GLfloat playerSizeY)
{
	bool inXdirection = ballX + ballR >= playerX && (playerX + playerSizeX >= ballX  && playerX - playerSizeX <= ballX) ;
	bool inYdirection = ballY + ballR >= playerY && (playerY + playerSizeY >= ballY  && playerY - playerSizeY <= ballY);

	return inXdirection && inYdirection;
}

GLfloat collMagnitude(GLfloat ballX, GLfloat ballR, GLfloat playerX)
{
	return ballX + ballR - playerX;
}

Game::Game(int width,int height,const std::string & title):width(width),height(height) {

	{
		glfwInit();
		glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
		glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
		glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GLFW_TRUE);
		glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
		glfwWindowHint(GLFW_SAMPLES, 0);
		glfwWindowHint(GLFW_RED_BITS, 8);
		glfwWindowHint(GLFW_GREEN_BITS, 8);
		glfwWindowHint(GLFW_BLUE_BITS, 8);
		glfwWindowHint(GLFW_ALPHA_BITS, 8);
		glfwWindowHint(GLFW_STENCIL_BITS, 8);
		glfwWindowHint(GLFW_DEPTH_BITS, 24);
		glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
	}

	// Create a GLFWwindow object
	mainWindow = glfwCreateWindow(width,height,title.c_str(), nullptr, nullptr);
	glfwSetWindowUserPointer(mainWindow,this);

	if (mainWindow == nullptr) {
		cout << "Failed to create GLFW window" << endl;
		glfwTerminate();
		exit(-1);
	}
	glfwMakeContextCurrent(mainWindow);

	if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress))
	{
		cout << "Failed to initialize OpenGL context" << endl;
		exit(-1);
	}

	ImGui_ImplGlfwGL3_Init(mainWindow,false);

	//setup matrix
	{
		projectionMatrix = glm::ortho(0.0f,width*1.0f,0.0f,height*1.0f,-1.0f,1.0f);
	}

	glViewport(0,0, width, height);

	//compile shader
	{
		auto vs = fileToCharArr ("resources/sprite.vert");
		auto fs1 = fileToCharArr ("resources/sprite.frag");
		auto fs2 = fileToCharArr("resources/sprite2.frag");
		spriteProgram1 = makeProgram(compileShader(shDf(GL_VERTEX_SHADER,&vs[0],vs.size())),compileShader(shDf(GL_FRAGMENT_SHADER,&fs1[0],fs1.size())));
		spriteProgram2 = makeProgram(compileShader(shDf(GL_VERTEX_SHADER,&vs[0],vs.size())),compileShader(shDf(GL_FRAGMENT_SHADER,&fs2[0],fs2.size())));
	}

	glGenVertexArrays(2, VAO);
	glGenBuffers(2, VBO);
	glGenBuffers(1, &EBO);
}

void Game::run() {

	double last = 0;
	glfwSetTime(last);
	double delta = 0.0f;
	glfwSwapInterval(1);

	GLfloat x1 = -0.8f, y1 = 0.8f;
	GLfloat R = 0.02f; 
	GLfloat x2 = -0.1f, y2 = -0.75f, sizeX = 0.1f, sizeY = 0.025f;
	const GLfloat Pi = M_PI;
	GLfloat theta = (Pi * 7) / 4;
	GLint score = 0;
	while (!glfwWindowShouldClose(mainWindow)) {
		double curr = glfwGetTime();
		delta = curr-last;
		last = curr;
		//input polling
		glfwPollEvents();
		//update objects
		update(delta, x2);
		//draw them
		draw(x1, y1, R, x2, y2, score);

		// change the ball's position
		x1 += cos(theta) * 0.01f;
		y1 += sin(theta) * 0.01f;
		if (x1 > 1)
			x1 = -1;
		if(y1 < -1)
		{
			printf("Game over\n");
			glfwSetWindowShouldClose(mainWindow, GLFW_TRUE);
			// y1 = 1;
		}
		if(x1 < -1)
			x1 = 1;
		if(y1 > 1)
			y1 = -1;


		glfwSwapBuffers(mainWindow);

		if(checkCollision(x1, y1, R, x2, y2, sizeX, sizeY))
		{
			GLfloat mag = collMagnitude(x1, R, x2);
			theta = 2 * Pi - theta;
			theta += (mag - 0.5) * Pi / 4;
			printf("%f\n", collMagnitude(x1, R, x2));
			score += 1;
		}

	}

}

Game::~Game() {
	glfwTerminate();
}

void Game::update(double delta, GLfloat &x) {
	if (glfwGetKey(mainWindow, GLFW_KEY_ESCAPE) == GLFW_PRESS)
		glfwSetWindowShouldClose(mainWindow, GLFW_TRUE);
	else if(glfwGetKey(mainWindow, GLFW_KEY_RIGHT) == GLFW_PRESS)
	{
		x = (GLfloat)(x + 0.025) > (GLfloat)(1 - 0.1) ? (GLfloat)(1 - 0.1) : (GLfloat)(x + 0.025);
	}
	else if(glfwGetKey(mainWindow, GLFW_KEY_LEFT) == GLFW_PRESS)
	{
		x = ((GLfloat)(-1 + 0.1) > (GLfloat)(x - 0.025)) ? (GLfloat)(-1 + 0.1) : (GLfloat)(x - 0.025);
	}
}

void Game::draw(GLfloat x1, GLfloat y1, GLfloat R, GLfloat x2, GLfloat y2, GLint score) {

	glClearColor(0.0f,0.0f,0.0f,1.0f);

	glClear(GL_COLOR_BUFFER_BIT);

	drawShape(x1, y1, 0,  R, 1000);
	drawPlayer(x2, y2, 0);
	showScore(score);

}


void Game::showScore(int score) {

	ImGui_ImplGlfwGL3_NewFrame();
	ImGui::SetNextWindowSize(ImVec2(100, 100), ImGuiSetCond_FirstUseEver);

	ImGui::SetNextWindowPos(ImVec2(690,0));
	bool show_another_window = true;
	ImGui::Begin("Score", &show_another_window,ImGuiWindowFlags_NoTitleBar|ImGuiWindowFlags_NoResize);

	ImGui::Text("Score %d    ",score);

	ImGui::End();
	ImGui::Render();

}

void Game::	drawShape(GLfloat x, GLfloat y, GLfloat z, GLfloat R, GLint numSides)
{
	GLint k = numSides;
	GLint v = k + 2;

	GLfloat X[v], Y[v], Z[v];

	X[0] = x; Y[0] = y; Z[0] = z;

	GLfloat twoPi = 2 * M_PI;

	for(int i = 1; i < v; i++)
	{
		X[i] = x + R * cos((i * twoPi) / k);
		Y[i] = y + R * sin((i * twoPi) / k);
		Z[i] = z;
	}

	GLfloat shapeVertices[3 * v];

	for(int i = 0; i < v; i++)
	{
		shapeVertices[i * 3] = X[i];
		shapeVertices[i * 3 + 1] = Y[i];
		shapeVertices[i * 3 + 2] = Z[i];
	}

	glBindBuffer(GL_ARRAY_BUFFER, VBO[0]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(shapeVertices), shapeVertices, GL_STATIC_DRAW);
	glBindBuffer(GL_ARRAY_BUFFER, 0);


	glBindVertexArray(VAO[0]);
	glBindBuffer(GL_ARRAY_BUFFER, VBO[0]);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid *) 0);
	glEnableVertexAttribArray(0);
	glBindVertexArray(0);

	glUseProgram(spriteProgram1);
	glBindVertexArray(VAO[0]);
	glDrawArrays(GL_TRIANGLE_FAN, 0, numSides);
	glBindVertexArray(0);

}

void Game::drawPlayer(GLfloat x, GLfloat y, GLfloat z)
{
	GLfloat vertices[] = {
		x, y, z,
		x - 0.1f, y + 0.025f, z, 
		x + 0.1f, y + 0.025f, z,
		x + 0.1f, y - 0.025f, z, 
		x - 0.1f, y - 0.025f, z
	};

	GLuint indices[] = {
		0, 1, 2,
		0, 2, 3,
		0, 3, 4,
		0, 4, 1
	};

	glBindVertexArray(VAO[1]);

    glBindBuffer(GL_ARRAY_BUFFER, VBO[1]);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glBindBuffer(GL_ARRAY_BUFFER, 0); 

    glBindVertexArray(0); 

	glUseProgram(spriteProgram2);
	glBindVertexArray(VAO[1]);
	glDrawElements(GL_TRIANGLES, 12, GL_UNSIGNED_INT, 0);
	glBindVertexArray(0);
}