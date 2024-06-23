"""empty message

Revision ID: 932bc46b2bac
Revises: 
Create Date: 2024-06-23 16:22:33.951795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '932bc46b2bac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=250), nullable=True),
    sa.Column('fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('facts')
    # ### end Alembic commands ###
