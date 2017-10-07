#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <stdio.h>

using namespace std;

// vertex shader for drawing both ball and player
const GLchar * vertexShaderSource = "#version 330 core\n"
	"layout (location = 0) in vec3 position;\n"
	"void main()\n"
	"{\n"
	"gl_Position = vec4(position.x, position.y, position.z, 1.0);\n"
	"}\0";

// fragment shader to color the ball
const GLchar * fragmentShaderSourceBall = "#version 330 core\n"
	"out vec4 color;\n"
	"void main()\n"
	"{\n"
	"color = vec4(1.0f, 0.5f, 0.5f, 1.0f);\n"
	"}\n\0";

// fragment shader to color the rectangle (ball)
const GLchar * fragmentShaderSourceRect = "#version 330 core\n"
	"out vec4 color;\n"
	"void main()\n"
	"{\n"
	"color = vec4(1.0f, 0.5f, 0.2f, 1.0f);\n"
	"}\n\0";


// draws a circle with center (x, y, z) of radius R
void DrawBall(GLfloat x, GLfloat y, GLfloat z, GLfloat R);

int main(int argc, char *argv[])
{
	GLFWwindow *mainWindow = nullptr;
	int width = 800, height = 600;

	// setting up the environment
	{

		// window setup
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
		mainWindow = glfwCreateWindow(width,height,"try1", nullptr, nullptr);

		if(!mainWindow)
		{
			printf("Failed to create window\n");
			glfwTerminate();
			return -1;
		}
		glfwMakeContextCurrent(mainWindow);

		if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress))
		{
			printf("Failed to initialize OpenGL context\n");
			exit(-1);
		}


	}


}

