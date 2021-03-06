"""empty message

Revision ID: 70458ea493d1
Revises: edfb363b34cd
Create Date: 2021-09-19 19:01:26.733307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70458ea493d1'
down_revision = 'edfb363b34cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('height', sa.String(length=10), nullable=True),
    sa.Column('hair_color', sa.String(length=30), nullable=True),
    sa.Column('skin_color', sa.String(length=30), nullable=True),
    sa.Column('birth_year', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('rotation_period', sa.String(length=10), nullable=True),
    sa.Column('climate', sa.String(length=30), nullable=False),
    sa.Column('terrain', sa.String(length=30), nullable=True),
    sa.Column('population', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
