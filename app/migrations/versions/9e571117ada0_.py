"""empty message

Revision ID: 9e571117ada0
Revises: c6456eb38cae
Create Date: 2020-02-22 22:37:10.831201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e571117ada0'
down_revision = 'c6456eb38cae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('block',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('block', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('to_whom', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('block')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('block')
    # ### end Alembic commands ###
