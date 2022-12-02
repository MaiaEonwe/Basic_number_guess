
import random as rand
def number_guess():# scale of the numbers between0-100
    counter=0
    scale_start=int(input("SAyı başlangıcı"))
    scale_finish=int(input("Sayı son"))
    target=int(input("Tahmin edilmesini istediniz sayıyı girininz"))
    guess=rand.randint(scale_start,scale_finish)
    while True:
        try: 
            if target==guess:
                counter+=1
                print(f"{counter}. denemede bulundu hedef sayı ise {target}")
                break
            elif target<guess:
                counter+=1
                scale_finish=(scale_finish)/2
                guess=rand.randint(round(scale_start),round((scale_finish)/2))
                print(guess)
            elif target>guess:
                counter+=1
                scale_start=scale_finish/2
                guess=rand.randint(round(scale_start),round(scale_finish))
                print(guess)
        except ValueError:
            print(f"{counter}. denemede bulundu hedef sayı ise {target}")
            break
            

number_guess()

        
