#include <glad/glad.h>
#include <glm/gtc/type_ptr.hpp>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include "glm/ext.hpp"
#include "tvp.hpp"
#include <iostream>
// #include "glm/gtx/string_cast.hpp"

void print(glm::mat4 M)
{
	std::cout << M[0].x << " " << M[0].y << " " << M[0].z << " " << M[0].w << "\n" ;
	std::cout << M[1].x << " " << M[1].y << " " << M[1].z << " " << M[1].w << "\n" ;
	std::cout << M[2].x << " " << M[2].y << " " << M[2].z << " " << M[2].w << "\n" ;
	std::cout << M[3].x << " " << M[3].y << " " << M[3].z << " " << M[3].w << "\n" ;
}


//TODO implement this functions for part 2
glm::mat4 myLookAt(const glm::vec3 eye, const glm::vec3 center, const glm::vec3 up)
{
    //TODO:your look at definition
	glm::vec3 camDir = glm::normalize(eye - center);
	glm::vec3 camRight = glm::normalize(glm::cross(up, camDir));
	glm::vec3 camUp = glm::normalize(glm::cross(camDir, camRight));
    glm::mat4 lookMat = glm::mat4();
    lookMat[0] = glm::vec4(camRight, 0.0f);
    lookMat[1] = glm::vec4(camUp, 0.0f);
    lookMat[2] = glm::vec4(camDir, 0.0f);
    lookMat[3] = glm::vec4(0.0f, 0.0f, 0.0f, 1.0f);
    // std::cout << "lookMat : " <<  std::endl; 
    // print(lookMat);
    // std::cout << std::endl;
    glm::mat4 support = glm::mat4(1.0f);
    // a = glm::normalize(a);
    float l = glm::length(eye);
    glm::vec3 a = glm::vec4(0.0, 0.0, -l, 1.0);
    support[3] = glm::vec4(a, 1.0f);
    support = glm::transpose(support);
    // std::cout << "Support : " << std::endl;
    // print(support);
    // std::cout << std::endl;
    lookMat *= support;
    lookMat = glm::transpose(lookMat);
    return lookMat;
}

glm::mat4 getViewMatrix(){

    //TODO call your lookAt function here
    // std::cout << "glm LookAt : " << std::endl; 
    // print(latGiven);
    // std::cout << std::endl;
    glm::vec3 front = glm::vec3(100.0, 0.0, 0.0);
    glm::vec3 top = glm::vec3(0.0, 0.0, 100.0);
    glm::vec3 side = glm::vec3(0.0, 100.0, 0.0);
    glm::vec3 isometric = glm::vec3(100.0, 100.0, 100.0);
    glm::mat4 latGiven = glm::lookAt(isometric, glm::vec3(0.0, 0.0, 0.0), glm::vec3(0.0, 0.0, 1.0));
	glm::mat4 latMy = myLookAt(side, glm::vec3(0.0, 0.0, 0.0), glm::vec3(1.0, 0.0, 0.0));
	// std::cout << "my LookAt : " << std::endl;
	// print(latMy);
	// std::cout << std::endl;
	return latGiven;
    //Camera at (0, 0, 100) looking down the negative Z-axis in a right handed coordinate system
    // return  glm::lookAt(glm::vec3(0.0,0.0,100.0), glm::vec3(0.0, 0.0, 0.0), glm::vec3(0.0, 1.0, 0.0));
}


//TODO change projection matrix here
glm::mat4 getProjectionMatrix(float aspect, float height, float width) {
    float view_height = 100.0f;
    // glm::mat4 rot1 = glm::mat4(1.0f);
    // rot1 = glm::rotate(rot1, glm::radians(-30.0f), glm::vec3(0.0, 1.0, 0.0));
    glm::mat4 projection = glm::perspective(glm::radians(45.0f), (width) / (height), 0.1f, 1000.0f);
    // glm::mat4 rot2 = glm::mat4(1.0f);
    // rot2 = glm::rotate(rot2, glm::radians(30.0f), glm::vec3(0.0, 1.0, 0.0));
    // projection = rot1 * projection * rot2;
    // projection *= glm::perspective(glm::radians(45.0f), width / height, 0.1f, 1000.f);
    return projection;
}
