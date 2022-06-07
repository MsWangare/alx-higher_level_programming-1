#include "Python.h"
#include "stdio.h"

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: the
 *
 * Return: void function
 */

void print_python_list_info(PyObject *p)
{
	int i = 0;

	printf("[*] Size of the Python List = %d\n", (int) PyList_Size(p));
	printf("[*] Allocated = %d\n", (int) PyByteArray_Size(p));

	while((int) PyList_Size(p) > i)
	{
		if (PyLong_Check(PyList_GetItem(p, i)))
			printf("Element %d: int\n", i);
		else if (PyFloat_Check(PyList_GetItem(p, i)))
			printf("Element %d: float\n", i);
		else if (PyUnicode_Check(PyList_GetItem(p, i)))
			printf("Element %d: str\n", i);
		else if (PyList_Check(PyList_GetItem(p, i)))
			printf("Element %d: list\n", i);
		else if (PyTuple_Check(PyList_GetItem(p, i)))
			printf("Element %d: tuple\n", i);
		i++;
	}
}
