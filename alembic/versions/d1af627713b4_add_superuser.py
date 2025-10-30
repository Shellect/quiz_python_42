"""add_superuser

Revision ID: d1af627713b4
Revises: 5fdf40a37c9d
Create Date: 2025-10-30 16:28:42.556202

"""
import hashlib
import os
from typing import Sequence, Union

from alembic import op
from sqlalchemy import orm
import sqlalchemy as sa

from src.models.entities import Group, User

# revision identifiers, used by Alembic.
revision: str = 'd1af627713b4'
down_revision: Union[str, Sequence[str], None] = '5fdf40a37c9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def hash_paaword(password: str):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt.hex() + key.hex()

def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    admin_group = Group(name='admin', description='Admin group')
    users_group = Group(name='users', description='Regular users group')
    session.add(admin_group)
    session.add(users_group)
    session.flush()

    superuser = User(
        username='admin',
        email='admin@no_report.local',
        password_hash=hash_paaword('12345678'),
        group_id=admin_group.id,
        is_admin=True
    )
    session.add(superuser)
    session.commit()


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    session.execute(sa.text("DELETE FROM users WHERE username = 'superadmin'"))
    session.execute(sa.text("DELETE FROM groups WHERE name IN ('admin', 'users')"))
    session.commit()
