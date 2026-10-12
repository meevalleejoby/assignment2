
movies={
        "BKU":["10:00 AM",230],
        "Leo":["01:00 PM",230],
        "Asha":["05:00 PM",230]
}
def list_shows():
    print("------AVAILABLE SHOWS------")
    for i in movies:
        print(f"Name:{i}\tTime:{movies[i][0]}\tPrice:{movies[i][1]}")
    return list(movies.keys())

def book_tickets(show_name,no_of_tickets,*seat_numbers):
    movie1,movie2,movie3=show_name
    print("-------BOOK TICKET------")
  
    n=int(input("Choose the show:\n1.BKU\n2.Leo\n3.Asha\n"))
    
    if n==1:
        print(f"Name:{movie1}")
        no_of_tickets=int(input("No of tickets: "))
        seat_numbers=[]
        for i in range(no_of_tickets):
            seat_number=int(input(f"Enter seat number {i + 1}: "))
            seat_numbers.append(seat_number)
        print(f"Booking successful!\nNo of tickets: {no_of_tickets}\nSeat numbers:{seat_numbers}")
    elif n==2:
        print(f"Name:{movie2}")
        no_of_tickets=int(input("No of tickets: "))
        seat_numbers=[]
        for i in range(no_of_tickets):
            seat_number=int(input(f"Enter seat number {i + 1}: "))
            seat_numbers.append(seat_number)
        print(f"Booking successful!\nNo of tickets: {no_of_tickets}\nSeat numbers:{seat_numbers}")
            
            
    elif n==3:
        print(f"Name:{movie3}")
        no_of_tickets=int(input("No of tickets: "))
        seat_numbers=[]
        for i in range(no_of_tickets):
            seat_number=int(input(f"Enter seat number {i + 1}: "))
            seat_numbers.append(seat_number)
        print(f"Booking successful!\nNo of tickets: {no_of_tickets}\nSeat numbers:{seat_numbers}")
           
    else:
        print("No movies available") 

    return show_name,no_of_tickets,*seat_numbers



def calculate_price(quantity,discount=0,price=230):
    print("-------PAYMENT DETAILS-----")
    
    def loyalty_discount(quantity, discount_per_pair=5):
        
            if quantity < 2:
                return 0
            if quantity>1 and quantity%2==0:
                 return discount_per_pair + loyalty_discount(quantity - 2, discount_per_pair)
    loyalty=loyalty_discount(quantity)
    n=int(input("Select Payment Mode:\n1.Cash\n2.GPay\n3.Credit Card\n"))
    if n==1:
        subtotal=price*quantity
        print(f"Discount applied: {discount+loyalty}")
        total=subtotal-(discount+loyalty)
        print(f"Total amount: {total}")
    elif n==2:
        subtotal=price*quantity+30
        print(f"Discount applied: {discount+loyalty}")
        total=subtotal-(discount+loyalty)
        print(f"Total amount(convenience fee Rs 30/-): {total}")
    elif n==3:
        subtotal=price*quantity
        discount=subtotal*.30
        print(f"Discount applied: {discount+loyalty}")
        total=subtotal-(discount+loyalty)
        print(f"Total amount: {total}")
    else:
        
        print("Invalid option")

    return quantity,total


def cancel_booking(quantity,total):
    print("------CANCEL BOOOKING------")
    refund=total
    print(f"Booking cancelled\nCash Refunded: {refund}")
    return quantity,total



def ticket_main(show_name=None,no_of_tickets=0,*seat_numbers,quantity=0,total=0):
    if show_name is None:
        show_name=list(movies.keys())

    while True:
        print("----------MOVIE TICKET BOOKING SYSTEM-----------")
        print("1.VIEW AVAILABLE MOVIES\n2.BOOK TICKET\n3.PAYMENT OPTIONS\n4.CANCEL BOOKING\n5.EXIT")
        n=int(input("Enter an option: "))

        if n==1:
            show_name=list_shows()
        elif n==2:
            
            
            show_name,no_of_tickets,*seat_numbers=book_tickets(
                show_name,no_of_tickets,*seat_numbers
            )
        elif n==3:
            if no_of_tickets > 0:
                quantity,total=calculate_price(no_of_tickets)
            else:
                print("Book tickets before selecting payment.")
        elif n==4:
            if quantity > 0:
                quantity,total=cancel_booking(quantity,total)
                quantity=0
                seat_numbers=()
                return quantity,seat_numbers
            else:
                print("No paid booking to cancel.")
        elif n==5:
            break
        else:
            print("Invalid options!!")

    return "Thank You"
print(ticket_main())












