day =  input("Enter Day : ")

match day : 
    case "Monday" | "Mon" :
        print("Start of the week")
    case "Friday" | "Fri" :
        print("Weekend is coming")
    case "Saturday" | "Sat" :
        print("Weekend started")
    case "Sunday" | "Sun" :
            print("Chill, it's Sunday")
    case _ :
          print("Yet another day")
