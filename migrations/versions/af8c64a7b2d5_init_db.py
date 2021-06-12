"""init db

Revision ID: af8c64a7b2d5
Revises: 
Create Date: 2021-06-12 15:49:07.407258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af8c64a7b2d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('surname', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('loans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('loan_sum', sa.Integer(), nullable=True),
    sa.Column('payment_rest', sa.Integer(), nullable=True),
    sa.Column('payment_rep_month', sa.Integer(), nullable=True),
    sa.Column('loan_active', sa.Boolean(), nullable=False),
    sa.Column('loan_delinquency', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('loans')
    op.drop_table('client')
    # ### end Alembic commands ###