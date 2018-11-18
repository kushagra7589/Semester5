// #include <glad/glad.h>
// #include <GLFW/glfw3.h>
// #include <imgui_impl_glfw_gl3.h>

// #include <iostream>

// const GLchar* vertexShaderSource = "#version 330 core\n"
// 		"layout (location = 0) in vec3 position;\n"
// 		"void main()\n"
// 		"{\n"
// 		"gl_Position = vec4(position.x, position.y, position.z, 1.0);\n"
// 		"}\0";
// const GLchar* fragmentShaderSource = "#version 330 core\n"
// 		"out vec4 color;\n"
// 		"void main()\n"
// 		"{\n"
// 		"color = vec4(1.0f, 0.2f, 0.5f, 0.1f);\n"
// 		"}\n\0";

// int main(int argc,char * argv[]) {

// 	GLFWwindow * mainWindow = nullptr;
// 	const int width = 800,height = 600;

// 	GLuint shaderProgram;
// 	GLuint VAO,VBO, EBO;

// 	{
// 		//create window here,load OpenGL function pointers
// 		{

// 			glfwInit();
// 			glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
// 			glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
// 			glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GLFW_TRUE);
// 			glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
// 			glfwWindowHint(GLFW_SAMPLES, 0);
// 			glfwWindowHint(GLFW_RED_BITS, 8);
// 			glfwWindowHint(GLFW_GREEN_BITS, 8);
// 			glfwWindowHint(GLFW_BLUE_BITS, 8);
// 			glfwWindowHint(GLFW_ALPHA_BITS, 8);
// 			glfwWindowHint(GLFW_STENCIL_BITS, 8);
// 			glfwWindowHint(GLFW_DEPTH_BITS, 24);
// 			glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
// 			mainWindow = glfwCreateWindow(width,height,"Lab1", nullptr, nullptr);


// 			if (mainWindow == nullptr) {
// 				printf("Failed to create GLFW window\n");
// 				glfwTerminate();
// 				exit(-1);
// 			}
// 			glfwMakeContextCurrent(mainWindow);


// 			if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress))
// 			{
// 				printf("Failed to initialize OpenGL context\n");
// 				exit(-1);
// 			}


// 		}

// 		GLboolean ans = GL_FALSE;
// 		glGetBooleanv(GL_CULL_FACE, &ans);
// 		printf("culling is %d\n", (int)(ans == GL_TRUE));


// 		ImGui_ImplGlfwGL3_Init(mainWindow,false);


// 		using namespace std;
// 		GLfloat vertices[] = {
// 				0.5f,  0.5f, 0.0f,  // top right
// 				 0.5f, -0.5f, 0.0f,  // bottom right
// 				-0.5f, -0.5f, 0.0f,  // bottom left
// 				-0.5f,  0.5f, 0.0f   // top left 
// 		};

// 		GLuint indices[] = {
// 			0, 1, 3,        //First triangle
// 			1, 2, 3         //Second triangle
// 		};

// 		GLfloat triangleVertices[] = {
// 			0.5f,  0.5f, 0.0f,  // top right
// 			0.5f, -0.5f, 0.0f,  // bottom right
// 			-0.5f, -0.5f, 0.0f,  // bottom left
// 		};

// 		GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
// 		glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
// 		glCompileShader(vertexShader);
// 		// Check for compile time errors
// 		GLint success;
// 		GLchar infoLog[512];
// 		glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
// 		if (!success) {
// 			glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
// 			printf("ERROR::SHADER::VERTEX::COMPILATION_FAILED\n%s\n",infoLog );
// 		}
// 		// Fragment shader
// 		GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
// 		glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
// 		glCompileShader(fragmentShader);
// 		// Check for compile time errors
// 		glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
// 		if (!success) {
// 			glGetShaderInfoLog(fragmentShader, 512, NULL, infoLog);
// 			printf("ERROR::SHADER::FRAGMENT::COMPILATION_FAILED\n%s\n",infoLog);
// 		}
// 		// Link shaders
// 		shaderProgram = glCreateProgram();
// 		glAttachShader(shaderProgram, vertexShader);
// 		glAttachShader(shaderProgram, fragmentShader);
// 		glLinkProgram(shaderProgram);
// 		// Check for linking errors
// 		glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);    
// 		if (!success) {
// 			glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
// 			printf("ERROR::SHADER::PROGRAM::LINKING_FAILED\n%s\n",infoLog);
// 		}
// 		glDeleteShader(vertexShader);
// 		glDeleteShader(fragmentShader);


// 		glGenVertexArrays(1, &VAO);
// 		glGenBuffers(1, &VBO);
// 		glGenBuffers(1, &EBO);

// 		glBindBuffer(GL_ARRAY_BUFFER, VBO);
// 		glBufferData(GL_ARRAY_BUFFER, sizeof(triangleVertices), triangleVertices, GL_STATIC_DRAW);
// 		glBindBuffer(GL_ARRAY_BUFFER, 0);


// 		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
// 		glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
// 		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

// 		glBindVertexArray(VAO);
// 		glBindBuffer(GL_ARRAY_BUFFER, VBO);
// 		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
// 		glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
// 		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid *) 0);
// 		glEnableVertexAttribArray(0);


// 		glBindVertexArray(0);

// 	}



// 	int I = 0;
// 	//loop
// 	{

// 		// printf("%s\n", );
// 		double last = 0, accumulator = 0;
// 		glfwSetTime(last);
// 		double delta = 0.0f;
// 		glfwSwapInterval(1);




// 		float f = 0.0f;
// 		while (!glfwWindowShouldClose(mainWindow)) {

// 			I++;

// 			if (glfwGetKey(mainWindow, GLFW_KEY_ESCAPE) == GLFW_PRESS)
// 				glfwSetWindowShouldClose(mainWindow, GLFW_TRUE);

// 			double curr = glfwGetTime();
// 			delta = curr - last;
// 			last = curr;
// 			accumulator += delta;
// 			if(I % 100 == 0)
// 				printf("%lf\n", accumulator);

// 			glfwPollEvents();
// 			//draw stuff here
// 			{


// 				{
// 					glClearColor(0.5, 0.2, 0.6, 0.5);
// 					//Clear color buffer
// 					glClear(GL_COLOR_BUFFER_BIT);
// 				}

				
// 					//draw your stuff
// 					// glUseProgram(shaderProgram);
// 					// glBindVertexArray(VAO);
// 					// glDrawElements(GL_TRIANGLES, 0, GL_FLOAT, 0);
// 					// glBindVertexArray(0);

// 					glBegin(GL_TRIANGLE_FAN);
// 						glVertex2f(0.0f,  0.5f);
// 						glVertex2f(-0.5f, 0.5f);
// 						glVertex2f(0.5f, -0.5f);
// 					glEnd();
// 					// glEnableClientState(GL_VERTEX_ARRAY);
// 					// // glEnableClientState(GL_VERTEX_ARRAY);
// 					// glVertexPointer(3, GL_FLOAT, 0, triangleVertices);
// 					// glDrawArrays(GL_TRIANGLE_FAN, 0, 3);
// 					// glDisableClientState(GL_VERTEX_ARRAY);
				

// 				{
// 					ImGui_ImplGlfwGL3_NewFrame();
// 					using namespace ImGui;
// 					SetNextWindowSize(ImVec2(200, 100));
// 					bool show_another_window = false;

// 					Begin("Test Window", &show_another_window);
// 					SliderFloat("float", &f, 0.0f, 1.0f);

// 					Text("Hello");
// 					if (Button("Button")) {
// 						printf("pressed hello button\n");
// 					}
// 					End();

// 					Render();

// 				}
// 			}




// 			glfwSwapBuffers(mainWindow);

// 		}

// 	}
// 	return 0;
// }

#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <imgui_impl_glfw_gl3.h>
#include <cmath>

#include <iostream>

const GLchar* vertexShaderSource = "#version 330 core\n"
        "layout (location = 0) in vec3 position;\n"
        "void main()\n"
        "{\n"
        "gl_Position = vec4(position.x, position.y, position.z, 1.0);\n"
        "}\0";
const GLchar* fragmentShaderSource = "#version 330 core\n"
        "out vec4 color;\n"
        "void main()\n"
        "{\n"
        "color = vec4(1.0f, 0.5f, 0.2f, 1.0f);\n"
        "}\n\0";









int main(int argc,char * argv[]) {

    GLFWwindow * mainWindow = nullptr;
    const int width = 800,height = 600;

    GLuint shaderProgram;
    GLuint VAO,VBO;

    //setup





        //create window here,load OpenGL function pointers
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
            mainWindow = glfwCreateWindow(width,height,"Lab1", nullptr, nullptr);


            if (mainWindow == nullptr) {
                printf("Failed to create GLFW window\n");
                glfwTerminate();
                exit(-1);
            }
            glfwMakeContextCurrent(mainWindow);


            if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress))
            {
                printf("Failed to initialize OpenGL context\n");
                exit(-1);
            }


        }

        GLboolean ans = GL_FALSE;
        glGetBooleanv(GL_CULL_FACE, &ans);
        printf("culling is %d\n", (int)(ans == GL_TRUE));


        ImGui_ImplGlfwGL3_Init(mainWindow,false);


        using namespace std;
        GLfloat vertices[] = {
                0.0f, 0.5f, 0.49f,  // Top Right
                0.5f, -0.5f, 0.49f,  // Bottom Right
                -0.5f, -0.5f, 0.49f,  // Bottom Left

        };

        GLint numVertices = 8;
        GLint sides = numVertices - 2;

        GLfloat circleVertices[3 * numVertices];

        GLfloat X[numVertices];
        GLfloat Y[numVertices];
        GLfloat Z[numVertices];

        X[0] = Y[0] = Z[0] = 0.0f;

        GLfloat twoPi = 2 * M_PI;

        for(int i = 1; i < numVertices; i++)
        {
            X[i] = 0.42 * cos(i * twoPi / sides);
            Y[i] = 0.42 * sin(i * twoPi / sides);
            Z[i] = 0.0f;
        } 

        for(int i = 0; i < numVertices; i++)
        {
            circleVertices[3 * i] = X[i];
            circleVertices[3 * i + 1] = Y[i];
            circleVertices[3 * i + 2] = Z[i];
        }

        GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
        glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
        glCompileShader(vertexShader);
        // Check for compile time errors
        GLint success;
        GLchar infoLog[512];
        glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
        if (!success) {
            glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
            printf("ERROR::SHADER::VERTEX::COMPILATION_FAILED\n%s\n",infoLog );
        }
        // Fragment shader
        GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
        glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
        glCompileShader(fragmentShader);
        // Check for compile time errors
        glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
        if (!success) {
            glGetShaderInfoLog(fragmentShader, 512, NULL, infoLog);
            printf("ERROR::SHADER::FRAGMENT::COMPILATION_FAILED\n%s\n",infoLog);
        }
        // Link shaders
        shaderProgram = glCreateProgram();
        glAttachShader(shaderProgram, vertexShader);
        glAttachShader(shaderProgram, fragmentShader);
        glLinkProgram(shaderProgram);
        // Check for linking errors
        glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
        if (!success) {
            glGetProgramInfoLog(shaderProgram, 51   2, NULL, infoLog);
            printf("ERROR::SHADER::PROGRAM::LINKING_FAILED\n%s\n",infoLog);
        }
        glDeleteShader(vertexShader);
        glDeleteShader(fragmentShader);


        glGenVertexArrays(1, &VAO);
        glGenBuffers(1, &VBO);


        glBindBuffer(GL_ARRAY_BUFFER, VBO);
        glBufferData(GL_ARRAY_BUFFER, sizeof(circleVertices), circleVertices, GL_STATIC_DRAW);
        glBindBuffer(GL_ARRAY_BUFFER, 0);


        glBindVertexArray(VAO);
        glBindBuffer(GL_ARRAY_BUFFER, VBO);
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid *) 0);
        glEnableVertexAttribArray(0);


        glBindVertexArray(0);





    //loop
    {
    	GLint V = numVertices;

        double last = 0, accumulator = 0;
        glfwSetTime(last);
        double delta = 0.0f;
        glfwSwapInterval(1);



        float f = 0.0f;
        while (!glfwWindowShouldClose(mainWindow)) {


            if (glfwGetKey(mainWindow, GLFW_KEY_ESCAPE) == GLFW_PRESS)
                glfwSetWindowShouldClose(mainWindow, GLFW_TRUE);

            double curr = glfwGetTime();
            delta = curr - last;
            last = curr;
            accumulator += delta;

            glfwPollEvents();
            //draw stuff here
            {


                {
                    glClearColor(0.5, 0.5, 0.5, 0.5);
                    //Clear color buffer
                    glClear(GL_COLOR_BUFFER_BIT);
                }

                {
                    //draw your stuff
                    glUseProgram(shaderProgram);
                    glBindVertexArray(VAO);
                    glDrawArrays(GL_TRIANGLE_FAN, 0, V);
                    glBindVertexArray(0);
                }

                {
                    ImGui_ImplGlfwGL3_NewFrame();

                    ImGui::SetNextWindowSize(ImVec2(200, 100));
                    bool show_another_window = false;

                    ImGui::Begin("Test Window", &show_another_window);
                    ImGui::SliderFloat("float", &f, 0.0f, 1.0f);

                    ImGui::Text("Hello");
                    if (ImGui::Button("Button")) {
                        printf("pressed hello button\n");
                    }
                    ImGui::End();

                    ImGui::Render();

                }
            }




            glfwSwapBuffers(mainWindow);

        }

    }
    return 0;
}

