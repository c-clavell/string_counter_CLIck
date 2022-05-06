import click

from collections import Counter



def counterX(str1):
    dict1=Counter(str1)
    set1=sorted(set(list(str1)))
    dict2={}
    for i in set1:
        dict2[i]=dict1[i]
    return dict2


@click.command()
@click.argument('input_string', type=str)
@click.option("--count_numbers", is_flag=True, help="You want to see the numbers in the string" )
@click.option("--count_letters", is_flag=True, help="You want to see number of letters")
def main(input_string,count_numbers,count_letters):
    if count_numbers:
        n=sum(map(str.isnumeric, input_string))
        click.echo(f"Total numbers {n}")

        for key,value in counterX(input_string).items():
            if key.isnumeric():
                print("'",key,"'",":",value)

    elif count_letters:
        n=sum(map(str.isalpha, input_string))
        click.echo(f"Total letters {n}")

        for key,value in counterX(input_string).items():
            if key.isalpha():
                print("'",key,"'",":",value)

    else :
        print(" char" ,":", "total")
        for key,value in counterX(input_string).items():
            if key.isalnum():
                print("'",key,"'",":",value)


if __name__=="__main__":
    main()