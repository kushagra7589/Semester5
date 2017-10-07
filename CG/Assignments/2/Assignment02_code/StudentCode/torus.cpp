#include <glad/glad.h>
#include <vector>
#include <glm/gtc/constants.hpp>
#include <cmath>

//TODO:create and draw torus here
//refer cube.cpp for example

#define PI_ 3.14159265358979323846

void createTorusObject(GLuint &torusVAO){

	GLuint VBO;

	GLint numSides = 8;
	GLint numT = 24;

	GLfloat X[numSides * 2 * (numT + 1)], Y[numSides * 2 * (numT + 1)], Z[numSides * 2 * (numT + 1)];
	GLfloat c = 1.0f, a = 0.1f;

	GLfloat twoPi = 2 * PI_;

	GLfloat s, t;
	GLfloat x, y, z;

	int cnt = 0;
	for(int i = 0; i < numSides; i++)
	{
		for(int j = 0; j <= numT; j++)
		{
			for(int k = 1; k >= 0; k--)
			{
				s = (j + k) % numSides + 0.5;
				t = j % numT;
				X[cnt] = (c + a * cos(s * twoPi / numSides)) * cos(t * twoPi / numT);
				Y[cnt] = (c + a * sin(s * twoPi / numSides)) * sin(t * twoPi / numT);
				Z[cnt] = a * sin(s * twoPi / numSides);
				cnt++;
			}
		}
	}

	GLfloat shapeVertices[3 * numSides * 2 * (numT + 1)];

	for(int i = 0; i < cnt; i++)
	{
		shapeVertices[i * 3] = X[i];
		shapeVertices[i * 3 + 1] = Y[i];
		shapeVertices[i * 3 + 2] = Y[i]; 
	}

	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(shapeVertices), shapeVertices, GL_STATIC_DRAW);
	glBindBuffer(GL_ARRAY_BUFFER, 0);


	glBindVertexArray(torusVAO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid *) 0);
	glEnableVertexAttribArray(0);
	glBindVertexArray(0);

}

void drawTorus(GLuint &torusVAO,GLuint program){
	int numSides = 400;
	glUseProgram(program);
	glBindVertexArray(torusVAO);
	glDrawArrays(GL_TRIANGLES, 0, numSides);
	glBindVertexArray(0);
}
