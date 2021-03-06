"""empty message

Revision ID: 61442698af61
Revises: daf2b462a2a4
Create Date: 2020-12-23 09:17:15.427286

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '61442698af61'
down_revision = 'daf2b462a2a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('adminAvatar', sa.String(length=255), nullable=True))
    op.add_column('admin', sa.Column('adminSex', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'admin', ['adminAvatar'])
    op.drop_column('admin', 'adminUserName')
    op.add_column('user', sa.Column('userAvatar', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('userSex', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'user', ['userAvatar'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'userSex')
    op.drop_column('user', 'userAvatar')
    op.add_column('admin', sa.Column('adminUserName', mysql.VARCHAR(length=128), nullable=True))
    op.drop_constraint(None, 'admin', type_='unique')
    op.drop_column('admin', 'adminSex')
    op.drop_column('admin', 'adminAvatar')
    # ### end Alembic commands ###
