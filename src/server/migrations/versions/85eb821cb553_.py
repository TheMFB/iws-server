"""empty message

Revision ID: 85eb821cb553
Revises: 
Create Date: 2018-07-01 20:43:26.139187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85eb821cb553'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('client', sa.String(length=64), nullable=True),
    sa.Column('product_area', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feature_title'), 'feature', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_feature_title'), table_name='feature')
    op.drop_table('feature')
    # ### end Alembic commands ###