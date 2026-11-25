with open ("data/hbb_dna.fasta", "r") as file:
    full_sequence = ""
    for line in file:
        clean_line = line.strip()
        if not clean_line.startswith(">"):
            full_sequence = full_sequence + clean_line

g_count = full_sequence.count("G")
c_count = full_sequence.count("C")
a_count = full_sequence.count("A")
t_count = full_sequence.count("T")
gc_percentage = ((g_count + c_count)/len(full_sequence)) * 100
at_percentage = ((a_count + t_count)/len(full_sequence))*100
rna_sequence = full_sequence.replace("T", "U")

with open ("results/report.txt", "w") as report:
    report.write(f" ---Human Beta-Globin (HBB) Content Analyzer---\n")
    report.write(f" total length of sequence: {len(full_sequence)}\n")
    report.write(f" Total G count:{g_count}\n")
    report.write(f" Total C count:{c_count}\n")
    report.write(f" Total A count:{a_count}\n")
    report.write(f" Total T count:{t_count}\n")
    report.write(f"GC percentage: {gc_percentage:.2f}%\n")
    report.write(f"AT percentage: {at_percentage:.2f}%\n")
    report.write(f"RNA Sequence: {rna_sequence}\n")