
#ifndef ASSIGNMENT1_GAME_HPP
#define ASSIGNMENT1_GAME_HPP



#include <glad/glad.h>
#include <string>
#include <glm/glm.hpp>
#include <memory>


class GLFWwindow;

class Game {

public:
    Game(int width,int height,const std::string & title = "MainWindow");



    void run();
    ~Game();


    int height;
    int width;
private:

    GLFWwindow * mainWindow = nullptr;
    GLuint VAO[2], VBO[2], EBO;
    void update(double delta, GLfloat &);
    void draw(GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLint);
    void drawShape(GLfloat x, GLfloat y, GLfloat z, GLfloat R, GLint numSides);
    void drawPlayer(GLfloat x, GLfloat y, GLfloat z);

private:

    GLuint spriteProgram1, spriteProgram2;

    glm::mat4 projectionMatrix;
    void showScore(int score);


};


#endif //ASSIGNMENT1_GAME_HPP
