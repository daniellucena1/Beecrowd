n = int(input())
for i in range(1,n+1):
    shel, raj = [str (i) for i in input().split()]
    shel = shel.lower()
    raj = raj.lower()
    if (shel == 'tesoura' and raj == 'papel') or (shel == 'papel' and raj == 'pedra') or (shel == 'pedra' and raj == 'lagarto') or (shel == 'lagarto' and raj == 'spock') or (shel == 'spock' and raj == 'tesoura') or (shel == 'tesoura' and raj == 'lagarto') or (shel == 'lagarto' and raj == 'papel') or (shel == 'papel' and raj == 'spock') or (shel == 'spock' and raj == 'pedra') or (shel == 'pedra' and raj == 'tesoura'):
        print(f"Caso #{i}: Bazinga!")
    elif (shel == 'papel' and raj == 'tesoura') or (shel == 'pedra' and raj == 'papel') or (shel == 'lagarto' and raj == 'pedra') or (shel == 'spock' and raj == 'lagarto') or (shel == 'tesoura' and raj == 'spock') or (shel == 'lagarto' and raj == 'tesoura') or (shel == 'papel' and raj == 'lagarto') or (shel == 'spock' and raj == 'papel') or (shel == 'pedra' and raj == 'spock') or (shel == 'tesoura' and raj == 'pedra'):
        print(f"Caso #{i}: Raj trapaceou!")
    elif shel == raj:
        print(f"Caso #{i}: De novo!")