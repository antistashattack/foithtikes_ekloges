

def foithtikes_ekloges(
    aponekrwsh_sullogwn, eksousia_stis_gs, sullogoi_tampela, kleinw_khnhmata,
    kata_tis_gnwshs, o_kosmos_xazos, anasugkrothsh_sullogwn, thetiko_protagma, 
    enantia_se_kubernhsh_susthma_ee, ereuna_gia_anagkes, sundesh_ergatiko, 
    antifasismos, patriarxia, polemos, diagrafes_didaktra, idiwtika_panep,
    upoxrhmatodothsh, katarg_asilou, mnhmonia_mexri_na_sbhsei_o_hlios_o_prasinos
):

    if aponekrwsh_sullogwn:
        return "Δεν μπορούμε να αγωνιστούμε χωρίς συλλόγους. Κάτσε σπίτι σου."

    if (
        diagrafes_didaktra and idiwtika_panep and upoxrhmatodothsh and 
        katarg_asilou and mnhmonia_mexri_na_sbhsei_o_hlios_o_prasinos
    ):
        return "ΠΑΣΟΚ"

    if (not eksousia_stis_gs and sullogoi_tampela and kleinw_khnhmata):
        return "ΠΚΣ"

    if (
        not eksousia_stis_gs and not thetiko_protagma and 
        kata_tis_gnwshs and o_kosmos_xazos
    ):
        return "Αναφη στο τετράγωνο / Ασυμμετρία"

    if (
        eksousia_stis_gs and anasugkrothsh_sullogwn and thetiko_protagma 
        and ereuna_gia_anagkes and sundesh_ergatiko and 
        antifasismos and not patriarxia and not polemos and 
        not diagrafes_didaktra and not idiwtika_panep and 
        not upoxrhmatodothsh and not katarg_asilou
        or enantia_se_kubernhsh_susthma_ee 
    ):
        return "Αντίσταση - ATTACK"

    else :
        return "ΑΝΑΠΟΦΑΣΙΣΤΟ! Πρέπει να συζητήσουμε από κοντά! Σε καλούμε στο τραπεζάκι της Αντίστασης στο Κάτω Πολυτεχνείο!"



def yes_no(question):
    while True:
        reply = input(question + " (ναι/οχι): ").strip().lower()
        if reply in ["ναι", "nai", "yes"]:
            return True
        elif reply in ["οχι", "όχι", "oxi", "no"]:
            return False
        else:
            print("Απάντησε με 'ναι' ή 'όχι'.")

def main():
    print("🗳️ Φοιτητικές Εκλογές - Ερωτηματολόγιο Θέσεων")
    print("-" * 50)

    answers = {
        "aponekrwsh_sullogwn": yes_no("Θες να απονεκρωθούν οι φοιτητικοί σύλλογοι;"),
        "eksousia_stis_gs": yes_no("Θες όλη η εξουσία να είναι στις Γενικές Συνελεύσεις;"),
        "sullogoi_tampela": yes_no("Οι φοιτητικοί σύλλογοι είναι ταμπέλες που τους κάνεις ό,τι θέλεις;"),
        "kleinw_khnhmata": yes_no("Κλείνεις κάθε χρόνο τα κινήματα;"),
        "kata_tis_gnwshs": yes_no("Είσαι κατά της γνώσης;"),
        "o_kosmos_xazos": yes_no("Πιστεύεις πως ο κόσμος είναι χαζός και δεν καταλαβαίνει αν πεις τη λέξη 'καπιταλισμός';"),
        "anasugkrothsh_sullogwn": yes_no("Θες ανασυγκρότηση φοιτητικών συλλόγων;"),
        "thetiko_protagma": yes_no("Έχεις θετικό πρόταγμα για το πανεπιστήμιο των αναγκών μας;"),
        "enantia_se_kubernhsh_susthma_ee": yes_no("Είσαι συνολικά ενάντια σε κυβέρνηση, σύστημα και Ε.Ε.;"),
        "ereuna_gia_anagkes": yes_no("Θες έρευνα και γνώση για τις κοινωνικές ανάγκες;"),
        "sundesh_ergatiko": yes_no("Θες σύνδεση του φοιτητικού με το εργατικό και τα ταξικά σωματεία;"),
        "antifasismos": yes_no("Είσαι ενάντια στον φασισμό;"),
        "patriarxia": yes_no("Στηρίζεις την πατριαρχία;"),
        "polemos": yes_no("Είσαι υπέρ του πολέμου;"),
        "diagrafes_didaktra": yes_no("Στηρίζεις διαγραφές και δίδακτρα στα μεταπτυχιακά;"),
        "idiwtika_panep": yes_no("Στηρίζεις ιδιωτικά πανεπιστήμια;"),
        "upoxrhmatodothsh": yes_no("Στηρίζεις υποχρηματοδότηση και έρευνα για στρατό και επιχειρήσεις;"),
        "katarg_asilou": yes_no("Είσαι υπέρ της κατάργησης του ασύλου;"),
        "mnhmonia_mexri_na_sbhsei_o_hlios_o_prasinos": yes_no("Στηρίζεις μνημόνια μέχρι να σβήσει ο ήλιος ο πράσινος;"),
    }

    result = foithtikes_ekloges(**answers)
    print("\n📢 Πρέπει να ψηφίσεις:", result)


if __name__ == "__main__":
    main()
