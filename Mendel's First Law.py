# http://rosalind.info/problems/iprb/
with open('datasets/rosalind_iprb.txt') as f:
    num_d, num_h, num_r = map(float, f.readline().split())

    total = num_d + num_h + num_r

    rr = (num_r / total) * ((num_r - 1) / (total - 1))
    hh = (num_h / total) * ((num_h - 1) / (total - 1))
    hr = ((num_h / total) * (num_r / (total - 1))) + ((num_r / total) * (num_h / (total - 1)))

    rec_prob = rr + hh * 0.25 + hr * 0.5
    print (1 - rec_prob)
