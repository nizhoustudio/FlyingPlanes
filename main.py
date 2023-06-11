import pygame
from entities.Plane import Plane
from entities.Alien import create_aliens, show_aliens, move_aliens
from entities.Bullet import Bullet, show_bullets, move_bullets
from utils.impact import impact
from utils.render import render
from utils.over import over


def init(__caption: str, __path: str, __size: tuple):
    pygame.init()
    pygame.display.set_caption(__caption)
    pygame.display.set_icon(
        pygame.image.load(__path)
    )
    return pygame.display.set_mode(__size)


if __name__ == "__main__":

    # 初始化窗口
    screen = init("打飞机", "./assets/images/icon.png", (800, 600))

    # 初始化背景音乐
    pygame.mixer.music.load("./assets/music/background.wav")
    pygame.mixer.music.play(-1)

    # 初始化击中音效
    boom = pygame.mixer.Sound("./assets/music/boom.wav")

    # 加载背景图
    bgImg = pygame.image.load("./assets/images/background.png")

    # 初始化飞机
    plane = Plane("./assets/images/plane.png", 400, 500, 0)

    # 初始化外星人
    aliens = create_aliens(6)

    # 初始化子弹组
    bullets = []

    # 初始化分数
    score = [0]

    # 控制游戏进行
    RUN = True

    # 控制游戏重开
    RESTART = False

    # 主循环
    while RUN:

        # 绘制背景
        screen.blit(bgImg, (0, 0))



        # 绘制飞机
        screen.blit(plane.img, (plane.x, plane.y))

        # 绘制外星人
        show_aliens(aliens, screen)

        # 绘制子弹
        show_bullets(bullets, screen)

        # 绘制分数
        render(str(score[0]), (0, 255, 0), screen, (0, 0))

        # 监听事件
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                RUN = False
            # 按键按下事件
            if event.type == pygame.KEYDOWN:
                # 飞机左移
                if event.key == pygame.K_LEFT:
                    plane.step = -2
                # 飞机右移动
                elif event.key == pygame.K_RIGHT:
                    plane.step = 2
                elif event.key == pygame.K_SPACE:
                    # 发射子弹
                    bullets.append(Bullet("./assets/images/bullet.png", plane.x, plane.y - 50, 2))

            # 按键弹起事件
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    # 飞机停止
                    plane.step = 0

            # 鼠标按下事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 300 < x < 500 and 300 < y < 325:
                    RESTART = True

        # 游戏结束检测
        if over(aliens):
            render("GAME OVER", (0, 255, 0), screen, (300, 200))
            render("RESTART ?", (0, 255, 0), screen, (300, 300))
            if RESTART:
                # 初始化外星人
                aliens = create_aliens(6)

                # 初始化子弹组
                bullets = []

                # 初始化分数
                score = [0]

                RESTART = False

        else:
            # 移动飞机
            plane.move(0, 736)

            # 移动外星人
            move_aliens(aliens)

            # 移动子弹组
            move_bullets(bullets)

            # 碰撞检测
            impact(aliens, bullets, score, boom)

        # 重绘画布
        pygame.display.update()
