"""empty message

Revision ID: ec8d00a0656d
Revises: 
Create Date: 2018-07-05 22:32:56.185956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec8d00a0656d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_features_title', table_name='features')
    op.drop_table('features')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('features',
    sa.Column('id', sa.VARCHAR(length=64), nullable=False),
    sa.Column('title', sa.VARCHAR(length=64), nullable=True),
    sa.Column('description', sa.VARCHAR(length=120), nullable=True),
    sa.Column('client', sa.VARCHAR(length=64), nullable=True),
    sa.Column('client_priority', sa.INTEGER(), nullable=True),
    sa.Column('target_date', sa.DATETIME(), nullable=True),
    sa.Column('product_area', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_features_title', 'features', ['title'], unique=False)
    # ### end Alembic commands ###
