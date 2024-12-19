#include <stdio.h>
#include <Python.h>


/**
 * print_python_bytes - print some basic info about Python bytes objects
 * @p: python object
 * Return: nothing
 **/
void print_python_bytes(PyObject *p)
{
  char *s;
  Py_ssize_t len, k;

  printf("[.] bytes object info\n");
  if (!PyBytes_Check(p))
    printf("  [ERROR] Invalid Bytes Object\n");
  else
    {
      PyBytes_AsStringAndSize(p, &s, &len);
      printf("  size: %lu\n", len);
      printf("  trying string: %s\n", s);
      if (len > 10)
	len = 10;
      else
	len++;
      printf("  first %lu bytes: ", len);
      for (k = 0; k < len - 1; k++)
	printf("%02x ", s[k] & 0xff);
      printf("%02x\n", s[len - 1] & 0xff);
    }
}


/**
 * print_python_list - print some basic info about Python lists
 * @p: python object
 * Return: nothing
 **/
void print_python_list(PyObject *p)
{
  Py_ssize_t k;
  PyObject *in_list;

  if (PyList_Check(p))
    {
      printf("[*] Python list info\n");
     printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
      printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
      for (k = 0; k < PyList_Size(p); k++)
	{
	  in_list = PySequence_GetItem(p, k);
	  printf("Element %lu: %s\n", k,
		 in_list->ob_type->tp_name);
	  if (strcmp(in_list->ob_type->tp_name, "bytes") == 0)
	    print_python_bytes(in_list);
	}
    }
}
