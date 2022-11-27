#include <stdio.h>
#include <stdarg.h>

int
sum(int val, ...)
{
	va_list	arglist;
	int		arg, total;

	total = val;

	va_start(arglist, val);

	while ((arg = va_arg(arglist, int)) != 0)
		total += arg;

	va_end(arglist);

	return total;
}

void
myerrmsg(char *format, ...)
{
	va_list	arglist;

	printf("Error: ");
	va_start(arglist, format);
	vprintf(format, arglist);
	va_end(arglist);
}

main()
{
	printf("Total sum: %d\n", sum(1, 2, 3, 4, 5, 0));
	myerrmsg("Too difficult(%d)\n", 2);
}
