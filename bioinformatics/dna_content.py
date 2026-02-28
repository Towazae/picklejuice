def main():
    dna = "ACTGCTAGCGCTATCGCTCGCTGC"
    test_dna = "ATCG"
    dna_gc = gc_content(dna)
    test_dna_gc = gc_content(test_dna)

    print(f"Test DNA GC content percentage is {test_dna_gc}%.")
    print(f"DNA GC content percentage is {dna_gc}%.")

def gc_content(seq: str) -> float:
    seq = seq.upper()
    g_count = seq.count("G")
    c_count = seq.count("C")
    return (g_count + c_count) / len(seq) * 100

main()