#include "main.h"
#include <stdio.h>

/**
  * binary_to_uint - Converts a binary number to an unsigned int
  * @b: The binary string to convert
  * Return: The positive converted number.
  */
unsigned int binary_to_uint(const char *b)
{
	int i;
	unsigned int value = 0;

	if (b == NULL)
		return (0);
	for (i = 0; b[i] != '\0'; i++)
	{
		if (b[i] != '0' && b[i] != '1')
			return (0);
	}
	for (i = 0; b[i] != '\0'; i++)
	{
		value = value << 1;
		if (b[i] == '1')
			value += 1;
	}
	return (value);
}

