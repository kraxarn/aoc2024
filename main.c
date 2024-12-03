#include <stdio.h>
#include <stdlib.h>
#include <regex.h>
#include <string.h>

#include "pocketpy.h"

static bool re_find_all(const int argc, py_Ref argv)
{
	PY_CHECK_ARGC(2);
	PY_CHECK_ARG_TYPE(0, tp_str);
	PY_CHECK_ARG_TYPE(1, tp_str);

	const char *pattern = py_tostr(py_arg(0));
	const char *string = py_tostr(py_arg(1));

	regex_t regex;
	regmatch_t p_match[1];
	size_t offset = 0;

	if (regcomp(&regex, pattern, REG_EXTENDED) != 0)
	{
		fprintf(stderr, "Failed to compile regex");
		return false;
	}

	py_newlist(py_retval());

	while (regexec(&regex, string + offset, 1, p_match, 0) == 0)
	{
		const size_t start = offset + p_match[0].rm_so;
		const size_t end = offset + p_match[0].rm_eo;
		const size_t len = end - start;

		char *match = malloc((len + 1) * sizeof(char));
		strncpy(match, string + start, len);
		match[len] = '\0';

		py_Ref reg = py_getreg(0);
		py_newstr(reg, match);
		py_list_append(py_retval(), reg);

		offset += p_match[0].rm_eo;
		free(match);
	}

	return true;
}

static bool read_lines(const int argc, py_Ref argv)
{
	PY_CHECK_ARGC(1);
	PY_CHECK_ARG_TYPE(0, tp_str);

	const char *path = py_tostr(py_arg(0));

	FILE *file = fopen(path, "r");
	if (file == nullptr)
	{
		return false;
	}

	char *line = nullptr;
	size_t len = 0;
	ssize_t read;

	py_newlist(py_retval());

	while ((read = getline(&line, &len, file)) != -1)
	{
		if (line[read - 1] == '\n')
		{
			line[read - 1] = '\0';
		}

		py_Ref reg = py_getreg(0);
		py_newstr(reg, line);
		py_list_append(py_retval(), reg);
	}

	fclose(file);
	return true;
}

int main(const int argc, const char **argv)
{
	if (argc != 2)
	{
		printf("Usage: %s <file>\n", argv[0]);
		return 1;
	}

	FILE *file = fopen(argv[1], "r");
	if (file == nullptr)
	{
		printf("Failed to open file: %s\n", argv[1]);
		return 1;
	}

	fseek(file, 0, SEEK_END);
	const long length = ftell(file);
	fseek(file, 0, SEEK_SET);

	char *buffer = malloc(length);
	if (buffer == nullptr)
	{
		printf("Failed to allocate memory for buffer\n");
		return 1;
	}

	fread(buffer, 1, length, file);

	py_initialize();

	py_Ref reg = py_getreg(0);

	py_newnativefunc(reg, read_lines);
	py_setglobal(py_name("read_lines"), reg);

	py_newnativefunc(reg, re_find_all);
	py_setglobal(py_name("re_find_all"), reg);

	const bool ok = py_exec(buffer, "<string>", EXEC_MODE, nullptr);

	if (!ok)
	{
		py_printexc();
	}

	fclose(file);
	free(buffer);
	py_finalize();

	return ok ? 0 : 1;
}
