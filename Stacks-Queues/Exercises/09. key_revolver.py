def shot_lock(bullets, locks):
    bullets.pop()
    locks.pop(0)
    print("Bang!")
    return bullets, locks

def missed_lock(bullets):
    bullets.pop()
    print("Ping!")
    return bullets

def shoot(bullets, locks, gun_barrel, bullet_count):
    if bullets[-1] <= locks[0]:
        shot_lock(bullets, locks)
    else:
        missed_lock(bullets)

def check_barrel(bullets_count, barrel, bullets):
    if bullets_count % barrel == 0 and bullets:
        print("Reloading!")

def print_result(locks, bullets, bullets_count, price_bullet, intelligence_value):
    if locks:
        print(f"Couldn't get through. Locks left: {len(locks)}")
    else:
        print(f"{len(bullets)} bullets left. Earned ${intelligence_value - bullets_count * price_bullet}")

price_bullet = int(input())
gun_barrel = int(input())
bullets = [int(el) for el in input().split()]
locks = [int(el) for el in input().split()]
intelligence_value = int(input())
bullet_count = 0

while bullets:
    if not locks:
        break
    shoot(bullets, locks, gun_barrel, bullet_count)
    bullet_count += 1
    check_barrel(bullet_count, gun_barrel, bullets)

print_result(locks, bullets, bullet_count, price_bullet, intelligence_value)