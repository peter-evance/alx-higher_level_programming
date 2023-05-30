#include "main.h"
#include <stdio.h>

/**
  * print_binary - Prints the binary representation of a number
  * @n: The number to representing in binary
  *
  * Return: Nothing
  */
void print_binary(unsigned long int n)
{
	if (n == 0)
	{
		_putchar('0');
		return;
	}

	divide(n);
}

/**
 * divide - prints binary represention for value 1.
 * @n: value.
 *
 * Return: Nothing.
 */
void divide(unsigned long int n)
{
	if (n < 1)
		return;

	divide(n >> 1);

	if (n & 1)
		_putchar('1');
	else
		_putchar('0');
}

