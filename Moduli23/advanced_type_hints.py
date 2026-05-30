from typing import Optional,Any,Union,List

def get_name(name: Optional[str] = None) -> str:  #funksioni optional munesh me vendos te dhenen e caktuar pershembull str ose munesh veq mos me shkru sen edhe apet nuk qet error

    if name:
        return name    #ky funskion i thot nese ka emer kthe emrin nese ska asni te dhan kthe Anonymous
    return "Anonymous"
print(get_name("Alea"))


#funskioni union te len me zgjedh mes dy te dhenave si ne ket rast duhet int ose string perndryshe qet error
def process_value(value: Union[int,str]) -> str:
    if isinstance(value,int):   #isintance o funskion i vete python ky funksion kontrrollon se a o vlera e njejte si mbrena kllapave
       return f"Number: {value}"
       return f"String: {value}"  #ky funksion thot nese vlera mbrenda kllapave o numer shfaqe vleren si numer dhe nese o fjal kthe si fjal
print(process_value(5))

#funksioni Any te len qfardo te dhene me vendos dhe nuk qet error
def process_anything(value: Any) -> str:
    return f"Processed: {value}"
print(process_anything(3))

#funksioni list te lejon te vendosesh ni grubull te dhenash ne forme liste
def sum_list(numbers: List[int]) -> int:
    return sum(numbers)      #ky funskion kthen shumen e numrave brenda kllapave pra i mbledh
result = sum_list([1,2,3,4,5])
print(f"Rezultati:{result}")

