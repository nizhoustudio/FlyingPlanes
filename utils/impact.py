def impact(aliens, bullets, score, boom):
    for alien in aliens:
        for bullet in bullets:
            if alien.x < bullet.x < alien.x + 50 and alien.y < bullet.y < alien.y + 50:
                alien.reset()
                bullets.remove(bullet)
                score[0] += 1
                boom.play()
