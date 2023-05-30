#include "main.h"

/**
 * get_endianness - Checks the endianness.
 *
 * Return: 0 if big endian
 *         else 1 for little endian.
 */
int get_endianness(void)
{
	int num = 1;
	char *endian = (char *)&num;

	if (*endian == 1)
		return (1);

	return (0);
}

