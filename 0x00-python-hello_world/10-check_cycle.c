#include "lists.h"
#include <stdlib.h>
#include <stdbool.h>
/**
 * check_cycle - check for the loop in a linked list
 * @list: data type listint_t pointer of list
 * Return: 0 if no cycle || 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first_loop;
	listint_t *second_loop;

	if (list == NULL || list->next == NULL)
/*No cycle in a list with 0 or 1 node */
		return  (false);

	first_loop = list->next;
	second_loop = list->next->next;

	while (first_loop && second_loop && second_loop->next)
	{
		if (first_loop == second_loop->next)
		{
/* cycle is  found in a list with 0 or 1 node */		
			return (true);
		}
		first_loop = first_loop->next;
		second_loop = second_loop->next->next;
	}
/* No cycle found*/
	return (false);
}

