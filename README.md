# MineSweeper

ITS 2024 - Progetto d'esame Python

Comandi per utilizzare git:

1) Clonare la repository, in modo da creare una copia locale dei file di github
    ```commandline
    git clone https://github.com/martinabruni/MineSweeper.git
    ```
2) Quando si comincia a lavorare sul progetto in locale, le modifiche non vanno in automatico su github, ma devono
   essere eseguiti alcuni passaggi:
    * Prima controlliamo i file che abbiamo modificato
   ```commandline
    git status
    ```
    * A questo punto aggiungere i file in un ambiente chiamato "Stage" (questo perche magari desideriamo salvarci le
      modifiche non di tutti i file ma solo di alcuni)
   ```commandline
    git add file1.py file2.py
    ```
    * Ora eseguire il commit, ovvero una fotografia dello stato dei file aggiungi in stage precedentemente. Il commit
      viene eseguito ancora localmente, eseguire il commit non significa aggiornare lo stato del progetto su github, ma
      solo sul pc che stiamo usando
    ```commandline
    git commit -m "Messaggio sensato"
    ```
    * Ora che abbiamo eseguito il commit, possiamo continuare a lavorare sul nostro progetto. Quando decidiamo di
      aggiornare lo stato del progetto su github eseguiamo il seguente comando:
   ```commandline
    git push
    ```
3) Se vediamo che il nostro branch e' indietro rispetto a quello in cloud (usando il comando ```git status```), lanciamo
   i comandi in quest'ordine:
    1) Prendiamo le modifiche fatte su github
   ```commandline
    git fetch
    ```
    2) E aggiorniamo il nostro branch locale
   ```commandline
    git pull
    ```
