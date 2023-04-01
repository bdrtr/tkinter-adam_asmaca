# Problem Seti 2, adamAsmaca.py
# İsim:
# Ortak çalışanlar:
# Harcanan zaman:

# Adam Asmaca Oyunu
#------------------------------------
# Yardımcı kod
# Bu yardımcı kodu anlamanıza gerek yok,
# ama fonksiyonları nasıl kullanacağını bilmeniz gerekecek
# (dökümanları okuduğunuzdan emin olun!)
import random
import string, os

WORDLIST_FILENAME = os.path.dirname(__file__)+"/kelimeler.txt"


def point_calculate(secret_word, rights):
    if int(rights)<0:
        rights=0

    return len(set(secret_word))*int(rights)

def load_words(path=WORDLIST_FILENAME):

    """
    Geçerli kelimelerin bir listesini döndürür.
    Kelimeler küçük harf dizileridir.
    
     Kelime listesinin boyutuna bağlı olarak,
     bu fonksiyonun tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi yükleniyor...")
    # inFile: file
    inFile = open(path, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yüklendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime döndürür
    """
    return random.choice(wordlist)

# yardımcı kodun sonu

#------------------------------------

# Programdaki herhangi bir yerden erişilebilmesi için
# kelime listesini değişken kelime listesine yükleyin

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime;
    tüm harflerin küçük olduğunu varsayar
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi);
     tüm harflerin küçük olduğunu varsayar
     returns: boolean, secret_word'ün tüm harfleri letter_guessed içindeyse True;
     Aksi takdirde yanlış
    '''
    for i in set(secret_word):
        if i not in list(letters_guessed):
            return False
    
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: harflerden, alt çizgilerden (_) ve şu ana kadar secret_word
     içindeki hangi harflerin tahmin edildiğini gösteren boşluklardan oluşan dize.
    '''

    char =""

    for i in secret_word:
        if i in letters_guessed:
            char+=i
        else:
            char+=' _ '

    return char



def get_available_letters(letters_guessed):
    '''
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: dize (harfler), hangi harflerin henüz tahmin edilmediğini temsil eden harflerden oluşur.
    '''

    chars = string.ascii_lowercase
    result=""
    for i in chars:
        if i not in list(letters_guessed):
            result+=i

    return result
    
    

def adamAsmaca(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyununu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini
        ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve
        kullanıcının henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir mektup yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    pass



# Adam asmaca işlevinizi tamamladığınızda, dosyanın
#en altına gidin ve test edilecek ilk iki satırın yorumunu kaldırın
# (ipucu: kendi testinizi yaparken kendi secret_word'ünüzü
# seçmek isteyebilirsiniz)

# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    other_word: string, normal İngilizce kelime
    returns: boolean, True, eğer my_word'ün tüm gerçek harfleri other_word'ün karşılık gelen harfleriyle eşleşiyorsa veya harf özel sembol _ ise ve my_word ile other_word aynı uzunluktaysa; Aksi takdirde False:
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    pass



def show_possible_matches(my_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    returns: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen
        her kelimeyi yazdırmalıdır.
    adamAsmaca ile bir harf tahmin edildiğinde, o harfin gizli kelimede
        geçtiği tüm pozisyonların ortaya çıktığını unutmayın.
    Bu nedenle, gizli harf(_ ) zaten ortaya çıkmış olan kelimedeki
     harflerden biri olamaz.
    '''
    ...



def adamAsmaca_ipuclu(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
     Etkileşimli bir Adam Asmaca oyunu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini ve
        kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır
    
     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve kullanıcının
        henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir harf tahmin ettiğini kontrol ettiğinizden emin olun.
      
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
      
     * Tahmin sembolü * ise, kelime listesindeki mevcut tahmin edilen
        kelimeyle eşleşen tüm kelimeleri yazdırın.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''



# adamAsmaca_ipuclu işlevinizi tamamladığınızda, yukarıdaki adam asmaca
# fonksiyonunu çalıştırmak için kullanılan benzer iki satırı yorumlayın ve
# ardından bu iki satırın yorumunu kaldırın ve test etmek için bu dosyayı çalıştırın!
# İpucu: Test ederken kendi secret_word'ünüzü seçmek isteyebilirsiniz.


if __name__ == "__main__":
    # pass

    # 2. bölümü test etmek için yukarıdaki pass satırında # işaretini kullanın ve aşağıdaki iki satırda # işaretini silin
    
    secret_word = choose_word(wordlist)
    adamAsmaca(secret_word)

    
###############
    
# 3. bölümü test etmek için yukarıdaki satırlarlarda yeniden # işaretini kullanın ve aşağıdaki iki satırda # işaretini silin

    #secret_word = choose_word(wordlist)
    #adamAsmaca_ipuclu(secret_word)
