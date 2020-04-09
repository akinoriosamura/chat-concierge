"""empty message

Revision ID: c2c4e95b8e0b
Revises: 
Create Date: 2020-04-06 21:24:12.775998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2c4e95b8e0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=False),
    sa.Column('prefer', sa.String(length=255), nullable=True),
    sa.Column('createTime', sa.DateTime(), nullable=False),
    sa.Column('updateTime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
