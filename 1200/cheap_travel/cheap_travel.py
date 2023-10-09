n, m, a, b = map(int, input().split())

m_tickets = n // m
m_cost = m_tickets * b
a_cost = n * a

if m_tickets == 0:
    total_cost = b if b < a_cost else a_cost
elif m_cost > a_cost:
    total_cost = a_cost
else:
    total_cost = m_cost
    rest_rides = n - (m * m_tickets)
    ar_cost = rest_rides * a

    total_cost += ar_cost if ar_cost < b else b

print(total_cost)