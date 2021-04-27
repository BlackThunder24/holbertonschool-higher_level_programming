#include "lists.h"
/**
 *check_cycle - prototype
 *@list: cycle.
 *Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *cycle, *cycle1;

	cycle = cycle1 = list;

	while (cycle && var2 && var2->next)
	{
		cycle = cycle->next;
		cycle1 = cycle1->next->next;

		if (cycle == cycle1)
			return (1);
	}
	return (0);
}
