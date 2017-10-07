
#include <glad/glad.h>
#include <glm/gtc/type_ptr.hpp>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

//TODO implement these functions for part 1
glm::mat4 rotateAroundZ(){

    glm::mat4 rot = glm::mat4(1.0f);
    rot = glm::rotate(rot, glm::radians(15.0f), glm::vec3(0.0, 0.0, 1.0));
    return rot;

}
glm::mat4 scaleAlongY(){

    glm::mat4 scal = glm::mat4(1.0f);
    scal = glm::scale(scal, glm::vec3(1.0, 2.0, 1.0));
    return scal;

}
glm::mat4 translateAlongXY(){

    glm::mat4 trans = glm::mat4(1.0f);
    trans = glm::translate(trans, glm::vec3(20, 10, 0));
    return trans;

}

glm::mat4 composeOrder1(){

    glm::mat4 trans = translateAlongXY();
    trans *= scaleAlongY();
    trans *= rotateAroundZ();
    return trans;

}
glm::mat4 composeOrder2(){

    glm::mat4 trans = rotateAroundZ();
    trans *= scaleAlongY();
    trans *= translateAlongXY();
    return trans;

}


glm::mat4 getModelMatrix()
{
    //Modelling transformations (Model -> World coordinates)
    glm::mat4 model = glm::mat4(1.0);

    //TODO: use the above functions here
    // model = rotateAroundZ();
    // model = scaleAlongY();
    // model = translateAlongXY();
    // model = composeOrder1();
    // model = composeOrder2();

    return model;

}
