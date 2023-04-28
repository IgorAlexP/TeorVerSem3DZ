"""Задача3
На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
 Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
 Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). 
 третьим спортсменом."""

 # Вероятность того, что выстрел произведен первым спортсменом
p_a = 0.9
# Вероятность того, что выстрел произведен вторым спортсменом
p_b = 0.8
# Вероятность того, что выстрел произведен третьим спортсменом
p_c = 0.6

# Вероятность попадания в мишень
p_hit = (p_a + p_b + p_c) / 3

# Вероятность того, что выстрел был произведен первым спортсменом
p_a_given_hit = p_a * p_hit / (p_a * p_hit + p_b * p_hit + p_c * p_hit)

# Вероятность того, что выстрел был произведен вторым спортсменом
p_b_given_hit = p_b * p_hit / (p_a * p_hit + p_b * p_hit + p_c * p_hit)

# Вероятность того, что выстрел был произведен третьим спортсменом
p_c_given_hit = p_c * p_hit / (p_a * p_hit + p_b * p_hit + p_c * p_hit)

print("Вероятность того, что выстрел был произведен первым спортсменом:", p_a_given_hit)
print("Вероятность того, что выстрел был произведен вторым спортсменом:", p_b_given_hit)
print("Вероятность того, что выстрел был произведен третьим спортсменом:", p_c_given_hit)