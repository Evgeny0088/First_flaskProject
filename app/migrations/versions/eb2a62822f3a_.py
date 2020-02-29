"""empty message

Revision ID: eb2a62822f3a
Revises: 3539e73f34fb
Create Date: 2020-02-23 01:21:36.253058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb2a62822f3a'
down_revision = '3539e73f34fb'
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
