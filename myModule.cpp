#include <Python.h>

//a func to calc factorial numbers
int cFib(int n)
{
    if (n<2) return n;
    return cFib(n-1) + cFib(n-2);
}

int cfactorial(int n)
{
	int result = 1;
	for(int i = 2; i <= n; i++)
		result *= i;
	return result;
}

int cError()
{
	//TODO: throw an excpetion and call PyErr_SetString, see: https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetString
	return -1;
}


static PyObject* fib(PyObject* self,PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args,"i",&n)) 
        return NULL;    
    return Py_BuildValue("i",cFib(n));
}

static PyObject* factorial(PyObject* self,PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args,"i",&n)) 
        return NULL;    
    return Py_BuildValue("i",cfactorial(n));
}

static PyMethodDef module_methods[] = {
    {"fib",(PyCFunction) fib, METH_VARARGS,"calculates the fibonachi number"},
	{"factorial",(PyCFunction) factorial, METH_VARARGS,"calculates the factorial of the number"},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef myModule =
{
    PyModuleDef_HEAD_INIT,
    "myModule", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    module_methods
};

PyMODINIT_FUNC PyInit_myModule(void)
{
    return PyModule_Create(&myModule);
}