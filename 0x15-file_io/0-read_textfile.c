#include "main.h"
#include <stdlib.h>

/**
 * read_textfile - Reads a text file and prints it to POSIX stdout.
 * @filename: The Source file
 * @letters: Number of letters to read and print.
 *
 * Return: If file cannot be opened/read | filename is NULL - 0.
 *         O/w - the actual number of bytes the function can read and print.
 */
ssize_t read_textfile(const char *filename, size_t letters)
{
	ssize_t openfile, readfile, writefile;
	char *buffer;

	if (filename == NULL)
		return (0);

	buffer = malloc(sizeof(char) * letters);
	if (buffer == NULL)
		return (0);

	openfile = open(filename, O_RDONLY);
	readfile = read(openfile, buffer, letters);
	writefile = write(STDOUT_FILENO, buffer, readfile);

	if (openfile == -1 || readfile == -1 ||
		writefile == -1 || writefile != readfile)
	{
		free(buffer);
		return (0);
	}

	free(buffer);
	close(openfile);

	return (writefile);
}

