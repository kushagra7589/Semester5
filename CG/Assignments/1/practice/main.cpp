#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <stdio.h>

void onWindowResize(GLFWwindow *window, int width, int height);

void processInput(GLFWwindow *window)
{
	if(glfwGetKey(window, GLFW_KEY_ENTER) == GLFW_PRESS)
	{
		printf("%s\n", "You pressed enter key");
	}
	else if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
	{
		glfwSetWindowShouldClose(window, true);
	}
}

int main()
{
	glfwInit();
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	GLFWwindow *window = glfwCreateWindow(800, 600, "First Window", NULL, NULL);

	if(window == NULL)
	{
		printf("%s\n", "Could not create window");
		glfwTerminate();
		return -1;
	}

	glfwMakeContextCurrent(window);


	if(!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
	{
		printf("%s\n", "Failed to initialise GLAD");
		return -1;
	}

	glViewport(0, 0, 800, 600);

	glfwSetFramebufferSizeCallback(window, onWindowResize);

	while(!glfwWindowShouldClose(window))
	{
		processInput(window);
		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT);
		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	glfwTerminate();
	return 0;
}

void onWindowResize(GLFWwindow *window, int width, int height)
{
	printf("You just resized the window to %d by %d\n", width, height);
	glViewport(0, 0, width, height);
}
