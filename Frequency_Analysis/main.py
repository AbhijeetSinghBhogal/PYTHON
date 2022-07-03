import matplotlib.pylab as plt

# Conda environment "env_testing"

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(text):
    
    text = text.upper()

    letter_frequencies = {}

    for letter in LETTERS:
        letter_frequencies[letter] = 0

    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    print(letter_frequencies)

    return letter_frequencies

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


if __name__ == '__main__':

    plain_text = "OOFWGTXYE - FKVY MHIULX WTOGLE TH AMBELFS MV XAIAAPL, KQSDAAPL, ZQROLD AGK YUVO YOKL - FONJT NXHDLR LHEKF MSILOT HM PABSK LBMQ IG AADT- F’E MHKQRG DAREK. FEVOZOEVSY BZ BOPLDEW UAT CBET UF EIEPOOG JTIIZ MN- W LXEVADIVPFY, UBF BR ATE VYQAMPHIMF MNW PZGXUGIMF AF VVYPNAQR LJUE- GAUSMZ IHH ADAGZXAML EOVPQTR’Z ZEXKE AGK IAGAE IGAA PKVPUVAE TAHF CTU UMIYAVX IATA ZACBLFY TUP TAL QCHUAMR."

    freq = frequency_analysis(plain_text)
    plot_distribution(freq)
