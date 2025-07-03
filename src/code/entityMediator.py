from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.playerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right <= 0:
                entity.health = 0
        if isinstance(entity, PlayerShot):
            if entity.rect.left >= WIN_WIDTH:
                entity.health = 0
        if isinstance(entity, EnemyShot):
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity: Entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)
