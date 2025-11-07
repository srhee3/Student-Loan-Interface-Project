#include <stdio.h>
#include <math.h>

int main()
{
    double b;
    printf("Please enter the amount of money you borrowed: $");
    scanf("%lf", &b);
    
    double ar;
    printf("Please enter the annual interest rate: ");
    scanf("%lf", &ar);
    double mo_ra = ar/12;
    
    int num;
    printf("Please enter the number of payments to be made: ");
    scanf("%d", &num);
    
    double payment = mo_ra*b/(1-pow(1+mo_ra,(-num)));
    double total_paid = payment*num;
    
    printf("A loan of $%.2lf with an annual interest of %.2lf payed off over %d months will have monthly payments of $%.2lf.",b,ar,num,payment);
    printf("\nIn total you will pay $%.2lf, making the cost of your loan $%.2lf.",total_paid,total_paid-b);
    
    return 0;
}


