#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    long int length;

    fflush(stdout);

    printf("[.] string object info\n");
    if (PyUnicode_Check(p))
    {
        length = PyUnicode_GET_LENGTH(p);
        if (PyUnicode_IS_ASCII(p))
            printf("  type: compact ascii\n");
        else
            printf("  type: compact unicode object\n");
        printf("  length: %ld\n", length);
        printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
    }
    else
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
}
