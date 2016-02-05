#include <iostream>
#include "Grader.h"

using std::cout; 
using std::cin;

Grader::Grader() {
	grade = 0;
};

void Grader::getGrade() {
	cout << "Enter your grade: ";
	cin >> grade;

	if (grade <= 100 && grade >= 90) {
		cout << "You got an A!";
	}
	else if (grade <= 89 && grade >= 80) {
		cout << "You got a B!";
	}
	else if (grade <= 79 && grade >= 70) {
		cout << "You got a C!";
	}
	else if (grade <= 69 && grade >= 60) {
		cout << "You got a D!";
	}
	else {
		cout << "You got an F!";
	}
}