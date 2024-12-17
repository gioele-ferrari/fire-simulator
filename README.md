# Forest Fire Simulator 🌲🔥

Questo progetto è stato sviluppato per esercitarsi con **Pygame** e Python, creando una simulazione interattiva di una foresta dove gli alberi crescono, prendono fuoco e si propagano nel tempo.

L'obiettivo è visualizzare in modo animato la dinamica di crescita della foresta e della diffusione del fuoco, permettendo di osservare come si evolve il sistema attraverso semplici regole probabilistiche.

---

## 🏁 Come iniziare

Segui questi passaggi per eseguire il progetto sul tuo computer:

1. **Clona il repository**: Scarica il progetto localmente con il seguente comando:

   ```bash
   git clone https://github.com/gioele-ferrari/fire-simulator.git
   ```

2. **Installa Pygame**: Assicurati di avere **Pygame** installato. Puoi farlo tramite pip:

   ```bash
   pip install pygame
   ```

3. **Entra nel progetto**: Entra nella cartella del progetto:

   ```bash
   cd fire-simulator
   ```

4. **Esegui il progetto**: Avvia lo script principale con Python:

   ```bash
   py main.py
   ```

---

## 🎮 Come funziona

- La foresta viene generata in modo casuale in base a una **densità di alberi** predefinita.  
- Clicca con il `mouse` per **piazzare** un falò.
- Premi `Space` per **avviare** la simulazione.
- Durante ogni iterazione della simulazione:  
  - Gli alberi possono **crescere** su celle vuote con una certa probabilità.  
  - Gli alberi esistenti possono **prendere fuoco** casualmente.  
  - Il fuoco si **propaga** agli alberi adiacenti.  
  - Dopo aver bruciato, gli alberi lasciano la cella vuota.  
- Premi `R` per **rigenerare** la foresta in modo casuale.

---

## 📋 Controlli

- **Mouse**: Metti il falò.
- **R**: Rigenera la foresta con una nuova mappa casuale.  
- **Space**: Avvia la generazione casuale del fuoco.  
- **Esc**: Chiudi la simulazione.
