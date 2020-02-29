"""empty message

Revision ID: c6456eb38cae
Revises: 383d6e05849c
Create Date: 2020-02-22 20:12:29.332563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6456eb38cae'
down_revision = '383d6e05849c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('block',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('to_whom', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('block')
    # ### end Alembic commands ###