

def clean_my_list(some_list):
    """ Puhastab antud nimekirja elentide algusest ja lõpust tühikud ning ravahetused 
    Args:
        some_list (list): Nimekiri, mis sisaldab puhastamata tekstielemente (nt faili read koos \n märgiga).
        
    Returns:
        list: Uus nimekiri, kus kõik elemendid on puhatstaud liigsetest tühikutest ja reavahetustest."""

    clean_list = []

    for element in some_list:
        clean_element = element.strip()
        clean_list.append(clean_element)

    return(clean_list)

