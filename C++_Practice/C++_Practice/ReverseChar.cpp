#include <iostream>

char* reverse(char *c) {
	char s;
	char *rev = c;

	while (*rev) ++rev;
	rev--;
	while (rev > c) {
		s = *c;
		*c++ = *rev;
		*rev-- = s;
	}

	return rev;
}
